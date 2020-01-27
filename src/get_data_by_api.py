# encoding = utf-8
import json

import requests


API = u'https://service-f9fjwngp-1252021671.bj.apigw.tencentcs.com/release/pneumonia'


class DataGetter:
	@staticmethod
	def getData(api):
		request = requests.get(url=api)
		print(request)

		return request.json()



if __name__ == '__main__':
	json_data = DataGetter.getData(api=API)
	print(json_data)