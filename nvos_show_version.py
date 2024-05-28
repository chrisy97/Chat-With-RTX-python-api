#!/usr/bin/env python3
import sys
import argparse
import netmiko

#return code
RET_CODE_SUCCESS                    = 0
RET_CODE_INVALID_PARAM_COUNT        = -1
RET_CODE_INVALID_PARAM              = -2

nvos_exp_admin = {
    'expect_string': rf"admin@.*:.*[#$] ",
    'strip_prompt':False,
    'strip_command':False,
    'read_timeout':60,
}
nvos_exp_root = {
    'expect_string': rf"root@.*:.*[#$] ",
    'strip_prompt':False,
    'strip_command':False,
    'read_timeout':60,
}

def run_command_on_nvos(ipaddr):
    print(f"Connecting to NVOS {ipaddr} ...")
    nvos_switch = {
        'device_type': 'linux',
        'ip': ipaddr,
        'username': 'admin',
        'password': 'admin',
    }
    net_connect = netmiko.ConnectHandler(**nvos_switch)
    output = net_connect.send_command("nv show system version", **nvos_exp_admin)
    print(output)
    net_connect.disconnect()

    return 0

# Entry function
if __name__ == '__main__':
    example_text = '''Example:
    Run commands on NVOS2.0:
        python {0} -p 10.7.144.34
    '''.format(sys.argv[0])

    parser = argparse.ArgumentParser(description='Run commands on NVOS2.0', epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-p', '--ip', type=str, help='The IP address of switch node', default=None)
    args = parser.parse_args()

    arg_ip = args.ip

    print("Input: IP addr {}".format(arg_ip))

    retry = False

    if (arg_ip is None):
        print("Please privide IP address of the target switch")
        print(example_text)
        exit(RET_CODE_INVALID_PARAM)

    # Update NVOS
    if arg_ip is None:
        print("Please provide the switch IP address to update NVOS")
        exit(RET_CODE_INVALID_PARAM)
    else:
        run_command_on_nvos(arg_ip)

    sys.exit(RET_CODE_SUCCESS)
