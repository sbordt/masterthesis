clear

load('/home/sbordt/Dropbox/Masterarbeit/masterthesis/data/giant_components/gc_0.mat')

x = zeros(length(P),1);
x(1) = 1.0;

tic()
for i = 1:10000
    x = P*x;
end
toc()

x(1)
x(2)
