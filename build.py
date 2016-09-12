# coding=utf-8
import os
import subprocess

#base cmd
java = "java360"
cmd = '-jar'
jar = 'jiagu/jiagu.jar'
#login
cmd_login = '-login'
name = ''
pwd = ''
#sign
cmd_sign = '-importsign'
key_path = ''
key_pwd = ''
alise = ''
alise_pwd = ''
#jiagu
cmd_jiagu = '-jiagu'
apkTarget = ''
apkOutPutPath = ''
#autosign
cmd_autosign = '-autosign'
#showsign
cmd_showsign = '-showsign'

#get target apk and keystore
for file in os.listdir('.'):
    if os.path.isfile(file):
        extension = os.path.splitext(file)[1][1:]
        if 'apk' in extension:
            apkTarget = os.path.basename(file)
        if "keystore" in extension:
            key_path = os.path.basename(file)

apkOutPutPath = os.getcwd()

auto_login_cmd = [java,cmd,jar,cmd_login,name,pwd]
auto_importsign_cmd = [java,cmd,jar,cmd_sign,key_path,key_pwd,alise,alise_pwd]
auto_show_sign_cmd = [java,cmd,jar,cmd_showsign]
auto_jiagu_sign_cmd = [java,cmd,jar,cmd_jiagu,apkTarget,apkOutPutPath,cmd_autosign]

subprocess.call(auto_login_cmd)
subprocess.call(auto_importsign_cmd)
subprocess.call(auto_show_sign_cmd)
subprocess.call(auto_jiagu_sign_cmd)
