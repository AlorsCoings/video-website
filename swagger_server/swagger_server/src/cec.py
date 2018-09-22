import subprocess


def turn_on_and_switch_tv():
    print('Turning on tv')
    subprocess.run('echo "on 0" | cec-client -s')
    print('Switching to raspberry pi input (1.0.0.0) for tv')
    subprocess.run('echo "tx 4F:82:10:00" | cec-client -s')
