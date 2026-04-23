from mininet.topo import Topo

class MyTopo(Topo):
    def build(self):
        # Create hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        # Create switch
        s1 = self.addSwitch('s1')

        # Create links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

# Topology dictionary (required by Mininet)
topos = {'mytopo': (lambda: MyTopo())}
