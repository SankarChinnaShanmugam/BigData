import matplotlib.pyplot as plt; plt.rcdefaults()
import pymongo
import networkx as nx
import matplotlib.pyplot as plt

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["WikiDBDetails"]
# mycol = mydb["WikiDBDetails"]
#  myresults = mycol.find({"References": {'$regex': ".*Biology.*"}})

myresults = {
#      "Qfit" ,"CP","MDR","aero","allel","beam","bio","blocks","build","chainer","chem","ci","cmeans","commpy",
# "credit","cuda","curve","cycling","data","dataaccess","datasets","dda","deploy","dsdp","ext","fda","fmm","fusion","fuzzy",
# "garden","geodesic","gof","gpuppy","grni","groups","gstat","gym","hep","image","intervals","keras","kinematics","learn",
# "maad","med","metrics","mlm","moletools","monaco","mps","nano","network","neuralnetwork","numerical","onnxruntime","opt"]
"applications","bicluster","calibration","classification","cluster","compose","covariance","cross_decomposition","datasets",
"decomposition","ensemble","exercises","feature_selection","gaussian_process","impute","inspection","linear_model","manifold",
"mixture","model_selection","multioutput","neighbors","neural_networks","preprocessing","semi_supervised","svm",
"text","tree","anomaly_comparison","changed_only_pprint_parameter","isotonic_regression","johnson_lindenstrauss_bound",
"kernel_approximation","kernel_ridge_regression","multilabel","multioutput_face_completion","roc_curve_visualization_api"}

r = 'Scikit Learn'
edges = []

for rr in myresults:
     edges.append((r, rr))

g = nx.DiGraph()
g .add_edges_from(edges)

plt.figure(figsize=(20, 10))

nx.draw(g, with_labels=True, node_size=5000, font_size=20)
plt.show()
