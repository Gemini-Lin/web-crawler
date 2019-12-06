#-*- coding:utf-8 -*-
from mininet.topo import Topo

class MyTopo(Topo):
	def __init__(self):
		
		Topo.__init__(self)
		host1=self.addHost('h1',ip="10.0.0.1")
		host2=self.addHost('h2',ip="10.0.0.2")
		host3=self.addHost('h3',ip="10.0.0.3")
		host4=self.addHost('h4',ip="10.0.0.4")
		host5=self.addHost('h5',ip="10.0.0.5")
		host6=self.addHost('h6',ip="10.0.0.6")
		host7=self.addHost('h7',ip="10.0.0.7")
		host8=self.addHost('h8',ip="10.0.0.8")
		switch1=self.addSwitch('s1')
		switch2=self.addSwitch('s2')
		switch3=self.addSwitch('s3')
		switch4=self.addSwitch('s4')
		switch5=self.addSwitch('s5')
		switch6=self.addSwitch('s6')
		
		self.addLink(host1,switch1)
		self.addLink(host2,switch1)
		self.addLink(host3,switch2)
		self.addLink(host4,switch2)
		self.addLink(host5,switch5)
		self.addLink(host6,switch5)
		self.addLink(host7,switch6)
		self.addLink(host8,switch6)
		self.addLink(switch1,switch3)
		self.addLink(switch3,switch5)
		self.addLink(switch2,switch4)
		self.addLink(switch4,switch6)
		self.addLink(switch1,switch4)
		self.addLink(switch3,switch6)
		self.addLink(switch3,switch2)
		self.addLink(switch4,switch5)
		
topos= {'mytopo':(lambda: MyTopo() )}
