function test2()
 n = 10000
 A = ones(n,n)
 B = ones(n,n)
 @time rand(4,4)*rand(4,4)
 @time C = A*B
end
test2()