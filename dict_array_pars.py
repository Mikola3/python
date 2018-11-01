# Распарсить отпут без хардкода: чтобы не было обращения к первому элементу массива.
resources = [{'OutputKey': 'StackZoneID', 'OutputValue': 'Z26RNL4JYFTOTI'}, {'OutputKey': 'Stack', 'OutputValue': 'UnitT-StackL-150ERKFTG-2e65e450.elb.us-east-1.amazonaws.com'}]

print(resources)
  for dict in resources:
    if 'OutputKey' in dict and dict['OutputKey'] == 'Stack':
      endpoint = dict['OutputValue']
  print(endpoint)

endpoint = [i['OutputValue'] for i in resources if i['OutputKey'] == 'Stack'][0]
