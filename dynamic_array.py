# modification in instance_id

# before
for i in range(3):
  instance_id = as_client.describe_auto_scaling_groups(AutoScalingGroupNames=[as_group])['AutoScalingGroups'][0]['Instances'][i]['InstanceId']
  #print(instance_id)
  ec2_client = boto3.client('ec2', region_name='${AWS::Region}')
  private_dns = ec2_client.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]['PrivateDnsName']
  #print(private_dns)
  dns.append(private_dns)
print(dns)

# after
instance_id = as_client.describe_auto_scaling_groups(AutoScalingGroupNames=[as_group])['AutoScalingGroups'][0]['Instances']
instance_ids = [i['InstanceId'] for i in instance_id]
print(instance_ids)

ec2_client = boto3.client('ec2', region_name='${AWS::Region}')
#private_dns = ec2_client.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]['PrivateDnsName']
for i in instance_ids:
  private_dns = ec2_client.describe_instances(InstanceIds=[i])['Reservations'][0]['Instances'][0]['PrivateDnsName']
  dns.append(private_dns)
print(dns)
