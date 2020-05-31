from bemaniproxy.node import Node

url_names = ["cardmng", "dlstatus", "eacoin", "facility" "message", "package", "pcbevent", "pcbtracker", "pkglist",
             "posevent", "lobby", "lobby2", "local", "local2", "apsmanager", "netlog"]


def item(name: str, url: str) -> Node:
    node = Node.void('item')
    node.set_attribute('name', name)
    node.set_attribute('url', url)
    return node


def create_services(data: Node, extra: dict) -> Node:
    root = Node.void("services")
    root.set_attribute("expire", "600")
    root.set_attribute("mode", "operation")
    root.set_attribute("product_domain", "1")

    for name in url_names:
        root.add_child(item(name, "http://{}/".format(extra.get("url"))))

    root.add_child(item("ntp", "ntp://pool.ntp.org/"))
    root.add_child(item(
        "keepalive",
        "ping://{0}/?pa={0}&amp;ia={0}&amp;ga={0}&amp;ma={0}&amp;t1=2&amp;t2=10".format(extra.get("url"))
    ))

    return root