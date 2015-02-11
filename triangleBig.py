import time

def makeBest (a) :
    # a is a list of lists - return altered list
    a[0][0] = max(a[0][0] + a[1][0], a[0][0] + a[1][1])
    return a
    
def sliceTriangle (s,i,j) :
    # s[i] slice a small triangle from a big one on a certain position, i,j makeBest and put back
    a = ([[s[i][j]],[s[i+1][j],s[i+1][j+1]]])
    a = makeBest(a)
    s[i][j] = a[0][0]
    s[i+1][j] = a[1][0]
    s[i+1][j+1] = a[1][1]
    return s

triangle = [map(int, row.split()) for row in open('/home/anke/EULER/#67/p067_triangle.txt').read().splitlines()]

# iter through the big triangle
start_time = time.time()
for line in range(len(triangle)) :
    # don't want to consider the bottom line
    if line > 0 :
        for element in range(len(triangle[-(line+1)])) :
            sliceTriangle (triangle,-(line+1),element)
end_time = time.time()
print 'Maximum path sum:', triangle[0][0]
print("Elapsed time was %g seconds" % (end_time - start_time))
