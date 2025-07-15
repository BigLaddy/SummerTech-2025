    self.Traveled.append(self.Current)
                pathfinder(Graph,self.Start,self.End,self.Current.edges[x],self.Traveled).FindPath()