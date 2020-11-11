import os

admin_server_name             = os.environ.get("ADMIN_NAME")
domain_path                   = os.environ.get("DOMAIN_HOME")

domainname = os.environ.get('DOMAIN_NAME', 'base_domain')
admin_name = os.environ.get('ADMIN_NAME', 'AdminServer')
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/' + domainname)

domain_name                   = os.environ.get("DOMAIN_NAME")
admin_port                    = int(os.environ.get("ADMIN_LISTEN_PORT"))
server_port                   = int(os.environ.get("MANAGED_SERVER_PORT"))
managed_server_name_base      = os.environ.get("MANAGED_SERVER_NAME_BASE")
number_of_ms                  = int(os.environ.get("CONFIGURED_MANAGED_SERVER_COUNT"))
domain_path                   = os.environ.get("DOMAIN_HOME")
cluster_name                  = os.environ.get("CLUSTER_NAME")
production_mode               = os.environ.get("PRODUCTION_MODE")

print('admin_name  : [%s]' % admin_server_name)
readDomain(domain_path)

# Init variables
fileStoreName = 'DistributedFileStore'
jmsServerName = 'DistributedJmsServer'
jmsSystemResourceName = '%s-JmsSystemRessource' % cluster_name
queueName = 'Q1'
subdeploymentName = '%s-SubDeployment' % cluster_name

cd('/')
cl=cmo.getClusters()[0]
filestore = create(fileStoreName, 'FileStore')
filestore.setDistributionPolicy('Distributed')
filestore.setTargets([cl])

jmsServer = create(jmsServerName, 'JMSServer')
jmsServer.setPersistentStore(filestore)
jmsServer.setTargets([cl])

jmsSystemResource = create(jmsSystemResourceName, 'JMSSystemResource')
jmsSystemResource.setTargets([cl])

cd('JMSSystemResource/%s/JmsResource/NO_NAME_0' % jmsSystemResourceName)
jmsQueue = create(queueName, 'UniformDistributedQueue')
jmsQueue.setJNDIName(queueName)
jmsQueue.setSubDeploymentName(subdeploymentName)

cd('/JMSSystemResource/%s' % jmsSystemResourceName)
subdeployment = create(subdeploymentName, 'SubDeployment')
subdeployment.setTargets([jmsServer])

updateDomain()
closeDomain()
exit()