#session
import boto3
aws_mg_con=boto3.session.Session(profile_name = 'Chandu_13')
#iam_con=aws_mg_con.resource('iam')
#list all iam users
#for each_user in iam_con.users.all():
    #print(each_user.name)
#print(dir(aws_mg_con))
#print(aws_mg_con.get_available_resources())
iam_con=aws_mg_con.client(service_name='iam', region_name='us-east-1')
for each_user in iam_con.list_users()["User"]:
    print(each_user['UserName'])
