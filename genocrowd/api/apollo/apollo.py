import time

from apollo import ApolloInstance
# from flask import current_app as ca

from flask import Blueprint, request, session
from flask import current_app as ca

from genocrowd.libgenocrowd.Data import Data
from genocrowd.libgenocrowd.Utils import Utils

import gridfs

apollo_bp = Blueprint('apollo', __name__, url_prefix='/')


@apollo_bp.route('/api/apollo/genechoice', methods=["GET"])
def annotation_start():
    """Selects a gene in MongoDB and imports it in the Annotation track

    Returns
    -------
    json
        url: url for the apollo window, centered on the gene position
        attributes: chromosome on which the gene is
    """
    DataInstance = Data(ca, session)
    all_positions = DataInstance.get_all_positions()
    selected_item = Utils.get_random_items(1, all_positions)[0]
    db = ca.mongo.db
    fs = gridfs.GridFS(db, collection="genes")
    gff_file = fs.get(selected_item["_id"])
    f = open("./gff.txt", mode="w")
    f.write(gff_file.read().decode('UTF-8'))
    f.close()
    f = open("./gff.txt", mode="r")
    apollo = ApolloInstance("http://localhost:8888", ca.apollo_admin_email, ca.apollo_admin_password)
    apollo.annotations.load_gff3("puceron_%s" % (session["user"]["email"]), f)
    time.sleep(1)
    url = "http://localhost:8888/annotator/loadLink?loc=%s:%s..%s&organism=puceron_%s" % (selected_item["chromosome"], selected_item["start"], selected_item["end"], session["user"]["email"])
    return {'url': url, 'attributes': selected_item["chromosome"]}


@apollo_bp.route('api/apollo/save', methods=["POST"])
def annotation_end():
    """gets the new annotation and saves it in mongodb"""
    data = request.get_json()
    apollo = ApolloInstance("http://localhost:8888", ca.apollo_admin_email, ca.apollo_admin_password)
    features = apollo.annotations.get_features(organism="puceron_%s" % (session["user"]["email"]), sequence=data["sequence"])["features"]
    with open("dump.json", 'w') as dump:
        dump.write(str(features))
    gff_file = apollo.annotations.get_gff3(features[0]["uniquename"], "puceron_%s" % (session["user"]["email"]))
    with open("GFF_OUT.gff", "w") as gffout:
        gffout.write(str(gff_file))
    DataInstance = Data(ca, session)
    DataInstance.store_answers_from_user(session["user"]["username"], gff_file)
    # apollo.organisms.delete_features("puceron_%s" % (session.user.email))
