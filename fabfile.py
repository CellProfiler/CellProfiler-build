# Fabric file that connects to a fresh virtual machine, sets up build
# dependencies, runs the build, and copies out the product and any
# error messages.
#
# Run with the IP address of the virtual machine in the -H
# parameter. Example: fab -H 192.168.194.177 build
#

from fabric.api import env, settings, run, put

env.key_filename = "../id_rsa"
env.user = "cpbuild"

def set_up_cpbuild_user():
    run("""test -d /home/cpbuild || adduser cpbuild""")
    run("""test -d /home/cpbuild/.ssh || sudo -u cpbuild mkdir -m 700 /home/cpbuild/.ssh""")
    put("%s.pub" % env.key_filename, 
        "/home/cpbuild/.ssh/authorized_keys", mode=0600)
    run("""chown cpbuild:cpbuild /home/cpbuild/.ssh/authorized_keys""")

def build():
    print env.hosts
    with settings(user="root"):
        set_up_cpbuild_user()
        put("deploy_build_root.sh", "~", mode=0755)
        run("./deploy_build_root.sh")
    put("deploy_build_cpbuild.sh", "~", mode=0755)
    run("./deploy_build_cpbuild.sh")


