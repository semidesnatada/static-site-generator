
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
        if self.tag == "img":
            out += f' style="width:100%"'
        return out

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        # elif self.tag == "code":
        #     return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        else:
            if not self.value:
                raise ValueError(f"No value to write in {self.tag}")
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
        if self.tag == "blockquote":
            out = f'<{self.tag}{self.props_to_html()}>'
            for child in self.children:
                out += f'<p>{child.to_html()}</p>'
            out += f'</{self.tag}>'
        else:
            out = f'<{self.tag}{self.props_to_html()}>'
            for child in self.children:
                out += child.to_html()
            out += f'</{self.tag}>'
        return out

        

