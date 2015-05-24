clear

load('/home/sbordt/Dropbox/Masterarbeit/masterthesis/data/giant_components/gc_0.mat')

x = zeros(1,length(P));
x(1) = 1.0;

tic()
for i = 1:10000
    x = x*P;
end
toc()

x(1)
x(2)