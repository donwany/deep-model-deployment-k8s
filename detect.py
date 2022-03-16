# from tensorflow.keras.applications.resnet50 import ResNet50
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
# import numpy as np

# model = ResNet50(weights='imagenet')


# img_path = '/Users/tsiameh/Desktop/denseNet/Mask_NoMask/train/MASK/awhhryrsvjdvwoncwmfdvoswcfzgou.png'


# def main():

#     img = image.load_img(img_path, target_size=(224, 224))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = preprocess_input(x)

#     preds = model.predict(x)
#     # decode the results into a list of tuples (class, description, probability)
#     # (one such list for each sample in the batch)
#     print('Predicted:', decode_predictions(preds, top=10)[0])

#     for pred in decode_predictions(preds, top=10)[0]:
#         print(pred)


# if __name__ == "__main__":
#     main()

# from kubernetes import client, config
#
# # Configs can be set in Configuration class directly or using helper utility
# config.load_kube_config()
#
# v1 = client.CoreV1Api()
# print("Listing pods with their IPs:")
# ret = v1.list_pod_for_all_namespaces(watch=False)
# for i in ret.items:
#     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))