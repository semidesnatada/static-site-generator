
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Called method on parent class. Call this function on a child class which inherits from this.")
        
    def props_to_html(self):    
        if self.props is None:
            return ""
        out = ''
        for key, value in self.props.items():
            out += f' {key}="{value}"'
        return out

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("No value to write")
        if not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Not a valid html tag")
        if self.children is None:
            raise ValueError("Children are missing")
        out = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            out += child.to_html()
        out += f'</{self.tag}>'
        return out

        

