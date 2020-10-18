import graphviz

def graphviz_elements(elements,filename):
    print("yo")
    D=graphviz.Digraph()
    D.format="svg"
    i=0
    
    for element in elements:
        
        #print(str(i),element.payload)
        style={"color":"black","shape":"box"}
        if element.style!=None:
            style.update(element.style)
        
        node=D.node(str(i),element.payload,**style)
        
        for x in element.out_connections:
            print(str(i),str(elements.index(x)))
            D.edge(str(i),str(elements.index(x)))
        i+=1
    #
    with D.subgraph() as S:
        S.attr(rank="same")
        S.node("3")
        S.node("5")
        
    D.render(filename)
    
def graphviz_FB_systems(systems,filename):
    D=graphviz.Digraph()
    D.format="svg"
    i=0
    si=0
    full_d_1={}
   # full_d_2={}
    for s in systems:
       
            for element in s.elements:
                
                print(str(i),element.payload)
                style={"color":"black","shape":"box"}#,"rank":}
                if element.style!=None:
                    style.update(element.style)
            
                node=D.node(str(i),element.payload,**style)
                full_d_1[element]=i
                #full_d_2[i]=element
                i+=1
                
    for s in systems:
        print(si,s)
        with D.subgraph(name="cluster_"+str(si)) as sub:
            sub.attr(label=s.name)#this should exist?
            sub.format=D.format
            for element in s.elements:
                for other in element.out_connections:
                    if other in s.elements:
                        #print(str(i),str(s.elements.index(x)))
                        print("sub")
                        sub.edge(str(full_d_1[element]),str(full_d_1[other]))
                    else:
                        print("global")
                        i2=full_d_1[element]
                        print(element.payload,other.payload)
                        print(full_d_1[element],full_d_1[other])
                        D.edge(str(full_d_1[element]),str(full_d_1[other]),rank="same")
                i+=1
                
            for pair in s.same_rank_pairs:
                with sub.subgraph() as sub2:
                    sub2.attr(rank="same")
                    print(pair[0].payload,pair[1].payload)
                    sub2.node(str(full_d_1[pair[0]]))
                    sub2.node(str(full_d_1[pair[1]]))
            #print("sub source?",sub.source)
            sub.render(filename+sub.name)
        si+=1
    D.render(filename)
    
if __name__=="__main__":
    durrhurr=True
