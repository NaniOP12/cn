from mininet.net import Mininet
from mininet.node import Controller
from mininet.topolib import TreeTopo
from mininet.cli import CLI
net = Mininet(controller= Controller)
h1=net.addHost('h1')
h2=net.addHost('h2')
h3=net.addHost('h3')
net.addLink(h1,h2)
net.addLink(h2,h3)
net.addLink(h3,h1)
net.start()
CLI(net)
net.stop()

