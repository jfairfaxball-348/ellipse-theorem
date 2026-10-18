#!/usr/bin/env python3
"""Reproduce TikZ figures and validate the nearest-predecessor example at 80 dps.
No random choices and no numerical tie assumptions. The exact heuristic counterexample
is independently checked in fractions. Run from paper/ directory.
"""
import json, math
from pathlib import Path
from fractions import Fraction as Q
import mpmath as mp
mp.mp.dps=80
OUT=Path('figures'); OUT.mkdir(exist_ok=True)
a=mp.mpf('1.01'); b=mp.mpf('1')
angles=list(map(mp.mpf,['0.14','0.59','1.30','1.95','2.68','3.22','3.94','4.65','5.34','5.89']))
pts=[(a*mp.cos(t),b*mp.sin(t)) for t in angles]; n=len(pts)
def d2(i,j):return sum((pts[i][k]-pts[j][k])**2 for k in (0,1))
def leg(x):return mp.nstr(x,17)
def seg(o,p,q):return (p[0]-o[0])*(q[1]-o[1])-(p[1]-o[1])*(q[0]-o[0])
def crosses(i,j,k,l):
 if len({i,j,k,l})<4:return False
 p,q,r,s=[pts[t] for t in (i,j,k,l)]
 return (seg(p,q,r)*seg(p,q,s)<0 and seg(r,s,p)*seg(r,s,q)<0)
def nearest_two(i,prev):
 return sorted(prev,key=lambda j:(d2(i,j),pts[j][0],pts[j][1]))[:2]
def ear(i,active):
 k=active.index(i); left=active[(k-1)%len(active)]; right=active[(k+1)%len(active)]
 others=[j for j in active if j!=i]
 return (set(nearest_two(i,others))=={left,right} and
         all(d2(i,j)>max(d2(i,left),d2(i,right)) for j in others if j not in (left,right)))
active=list(range(n)); deleted=[]; ear_info=[]
while len(active)>3:
 valid=[i for i in active if ear(i,active)]
 assert valid, ('no ear',active)
 # least admissible Euclidean two-step skip chord, if at least 5 points
 if len(active)>=5:
  lam=4*mp.atan(b/a)
  def span(i):
   k=active.index(i); lp=active[(k-1)%len(active)]; rp=active[(k+1)%len(active)]
   val=angles[rp]-angles[lp]
   return val if val>0 else val+2*mp.pi
  eligible=[i for i in active if span(i)<lam]
  assert eligible
  i=min(eligible,key=lambda x:d2(active[(active.index(x)-1)%len(active)],active[(active.index(x)+1)%len(active)]))
  assert i in valid, ('selected skip-chord index not metric ear',i,valid)
 else:
  i=min(valid)
 k=active.index(i); u=active[(k-1)%len(active)]; w=active[(k+1)%len(active)]
 ear_info.append(dict(site=i,remaining=list(active),neighbours=[u,w],
                     distances={str(j):leg(mp.sqrt(d2(i,j))) for j in active if j!=i}))
 deleted.append(i); active.remove(i)
seed=list(active); order=seed+list(reversed(deleted)); assert len(order)==n
edges=set(tuple(sorted(x)) for x in [(seed[0],seed[1]),(seed[1],seed[2]),(seed[0],seed[2])]); inserted={}
for pos,i in enumerate(order[3:],start=4):
 prev=order[:pos-1]
 pair=nearest_two(i,prev)
 expected=[]
 for info in ear_info:
  if info['site']==i: expected=info['neighbours']; break
 assert set(pair)==set(expected),(i,pair,expected)
 inserted[i]=pair
 for j in pair:
  e=tuple(sorted((i,j)));assert e not in edges;edges.add(e)
 assert all(not crosses(*x,*y) for x in edges for y in edges)
assert len(edges)==2*n-3
min_diff=min(abs(d2(i,j)-d2(i,k)) for i in range(n) for j in range(n) for k in range(j+1,n) if i not in (j,k))
assert min_diff>mp.mpf('1e-8')
# TikZ helper
coord=lambda p:'('+leg(mp.mpf(p[0].numerator)/p[0].denominator if isinstance(p[0],Q) else p[0])+','+leg(mp.mpf(p[1].numerator)/p[1].denominator if isinstance(p[1],Q) else p[1])+')'
def nodes(ids,labels=None,out=1.19):
 s=''
 for i in ids:
  x,y=pts[i]; t=angles[i]; lx=out*mp.cos(t);ly=out*mp.sin(t)
  s+=f'\\fill {coord((x,y))} circle (0.021);\\node[fill=white,inner sep=1pt,font=\\scriptsize] at {coord((lx,ly))} {{{labels[i] if labels else i}}};\n'
 return s
# main figure, standalone TikZ picture, 10 chronological sites
s='\\begin{tikzpicture}[scale=2.45,line cap=round]\n\\draw[gray!55,line width=.45pt] (0,0) ellipse (1.01 and 1);\n'
for i,j in sorted(edges):
 style='line width=.65pt,black' if i in seed and j in seed else 'line width=.43pt,gray!70!black'
 s+=f'\\draw[{style}] {coord(pts[i])} -- {coord(pts[j])};\n'
s+=nodes(range(n),{i:str(order.index(i)+1) for i in range(n)},1.18)
s+='\\end{tikzpicture}\n';(OUT/'headline.tikz').write_text(s)
# ear figure first deleted (strict metric ear)
item=ear_info[0];site=item['site'];u,w=item['neighbours'];remaining=item['remaining'];
s='\\begin{tikzpicture}[scale=2.35,line cap=round]\n'
poly=' -- '.join(coord(pts[i]) for i in remaining)+' -- cycle'
s+=f'\\fill[gray!10] {poly};\\draw[gray!70,line width=.6pt] {poly};\n'
s+=f'\\draw[very thick] {coord(pts[site])} -- {coord(pts[u])};\\draw[very thick] {coord(pts[site])} -- {coord(pts[w])};\n'
s+=f'\\draw[densely dashed,line width=.85pt] {coord(pts[u])} -- {coord(pts[w])};\n'
labels={j:(r'$v$' if j==site else (r'$u$' if j==u else (r'$w$' if j==w else ''))) for j in remaining}
for j in remaining:
 x,y=pts[j];t=angles[j];lx=1.19*mp.cos(t);ly=1.19*mp.sin(t)
 s+=f'\\fill {coord((x,y))} circle (.022);'
 if labels[j]:s+=f'\\node[fill=white,inner sep=1.2pt,font=\\small] at {coord((lx,ly))} {{{labels[j]}}};'
 s+='\n'
s+='\\end{tikzpicture}\n';(OUT/'metric-ear.tikz').write_text(s)
# derivative and three competitor bands schematic, all endpoints central closed
s=r'''\begin{tikzpicture}[x=0.71cm,y=0.71cm,>=stealth]
\draw[thick,->] (0,0) -- (12.1,0);
\fill[gray!8] (0,0.12) rectangle (3.5,.8);
\fill[gray!24] (3.5,.12) rectangle (8.5,.8);
\fill[gray!8] (8.5,.12) rectangle (12,.8);
\draw[dashed] (3.5,-.28) -- (3.5,1.1);
\draw[dashed] (8.5,-.28) -- (8.5,1.1);
\node[font=\small] at (1.75,.46) {forward (A)};
\node[font=\small] at (6,.46) {central (B)};
\node[font=\small] at (10.25,.46) {backward (C)};
\node[below,font=\scriptsize] at (0,0) {$0$};
\node[below,font=\scriptsize] at (3.5,0) {$\Lambda$};
\node[below,font=\scriptsize] at (8.5,0) {$2\pi-\Lambda$};
\node[below,font=\scriptsize] at (12,0) {$2\pi$};
\node[above,font=\scriptsize] at (6,1.0) {both boundary values belong to (B)};
\end{tikzpicture}
'''
(OUT/'competitor-bands.tikz').write_text(s)
# Four point cases: verify interior classification, convex ear
small=[[(0,0),(4,0),(.7,3.4),(.8,.9)],[(0,0),(4.5,0),(3.8,3.2),(.4,2.7)]]
# interior seed ABC insert D: DA, DB, DC squared
P=small[0];di=lambda a,b:sum((P[a][k]-P[b][k])**2 for k in [0,1]);assert set(sorted(range(3),key=lambda j:di(3,j))[:2])=={0,2}
P=small[1];di=lambda a,b:sum((P[a][k]-P[b][k])**2 for k in [0,1]);assert set(sorted([0,1,3],key=lambda j:di(2,j))[:2])=={1,3}
s='\\begin{tikzpicture}[x=.81cm,y=.81cm,line cap=round]\n'
for panel,offs in enumerate((0,5.8)):
 pp=small[panel]; q=lambda i:f'({pp[i][0]+offs},{pp[i][1]})'
 if panel==0:
  old=[(0,1),(1,2),(2,0)];new=[(3,0),(3,2)];last=3
 else:
  old=[(0,1),(1,3),(3,0)];new=[(2,1),(2,3)];last=2
 for i,j in old:s+=f'\\draw[gray!65,line width=.75pt] {q(i)} -- {q(j)};\n'
 for i,j in new:s+=f'\\draw[black,line width=1.15pt] {q(i)} -- {q(j)};\n'
 for i in range(4):
  s+=f'\\fill {q(i)} circle (.052);'
  loc='above' if i in (2,3) else 'below'
  s+=f'\\node[{loc},font=\\scriptsize] at {q(i)} {{$'+('D' if panel==0 and i==3 else 'C' if panel==1 and i==2 else 'ABCD'[i])+'$};\n'
 s+=f'\\node[below,font=\\small] at ({offs+2},-0.50) {{{"interior fourth site" if panel==0 else "convex quadrilateral"}}};\n'
s+='\\end{tikzpicture}\n';(OUT/'four-sites.tikz').write_text(s)
# exact rational heuristic counterexample
t=[Q(0),Q(1,3),Q(9,4),Q(113,50),Q(-9,4)]
rat=lambda t:(Q(101,100)*(1-t*t)/(1+t*t),2*t/(1+t*t))
p=[rat(z) for z in t]; d=lambda i,j:sum((p[i][k]-p[j][k])**2 for k in (0,1))
diff=d(2,1)-d(2,4);assert diff==Q(49482169,2352250000),diff
s='\\begin{tikzpicture}[scale=2.30,line cap=round]\n\\draw[gray!55] (0,0) ellipse (1.01 and 1);\n'
s+='\\draw[gray!60] '+' -- '.join(coord(pair) for pair in p)+' -- cycle;\n'
s+=f'\\draw[very thick] {coord(p[2])} -- {coord(p[4])};\n'
s+=f'\\draw[densely dashed,line width=1.0pt] {coord(p[2])} -- {coord(p[1])};\n'
for i,(x,y) in enumerate(p):
 norm=mp.sqrt(mp.mpf(x.numerator)**2/mp.mpf(x.denominator)**2+mp.mpf(y.numerator)**2/mp.mpf(y.denominator)**2)
 lx=mp.mpf(x.numerator)/x.denominator/norm*mp.mpf('1.2');ly=mp.mpf(y.numerator)/y.denominator/norm*mp.mpf('1.2')
 s+=f'\\fill {coord((x,y))} circle (.023);\n'
 if i not in (2,3):s+=f'\\node[font=\\scriptsize,fill=white,inner sep=1pt] at {coord((lx,ly))} {{$P_{i}$}};\n'
s+=r'''\node[font=\scriptsize,fill=white,inner sep=1pt] at (-.92,1.29) {$P_2,P_3$ (close)};
\draw[densely dotted] (-.683,.735) -- (-1.25,.9);
\draw[gray!70,rounded corners,fill=white] (-3.0,.20) rectangle (-1.25,1.55);
\node[font=\scriptsize] at (-2.13,1.37) {local detail ($120\times$)};
\fill (-2.26,.95) circle (.031);
\fill (-2.55,.69) circle (.031);
\node[font=\scriptsize,above right] at (-2.26,.95) {$P_2$};
\node[font=\scriptsize,below left] at (-2.55,.69) {$P_3$};
'''
s+='\\end{tikzpicture}\n';(OUT/'false-heuristic.tikz').write_text(s)
report={'precision_dps':80,'ellipse':{'a':'101/100','b':'1'},'angular_parameters_rad':[str(t) for t in angles],
        'arrival_order_site_indices':order,'seed_site_indices':seed,'deletion_order_site_indices':deleted,
        'insertion_nearest_predecessors':{str(k):v for k,v in inserted.items()},
        'all_edges':sorted(map(list,edges)),'edge_count':len(edges),'expected_edge_count':2*n-3,
        'proper_crossings':0,'min_squared_distance_comparison_margin':leg(min_diff),
        'strict_metric_ears':ear_info,
        'small_case_nearest_validation':{'interior':'D connects to A,C','convex':'C connects to B,D'},
        'heuristic_counterexample_exact_difference':str(diff),
        'heuristic_param_values':[str(z) for z in t]}
Path('scripts/figure-validation.json').write_text(json.dumps(report,indent=2)+'\n')
print('Validated example:',order,'edges',len(edges),'min distance-squared margin',mp.nstr(min_diff,8))
print('Ear witness first:',site,u,w)
print('Exact false-heuristic difference:',diff)
