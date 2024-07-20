import os
import time
source = [r'C:\Documents', r'C:\Work']
target_dir = '/Documents/'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr '%s %s" %(target, ''.join(source))

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
