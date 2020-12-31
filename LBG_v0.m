
%  https://github.com/internaut/py-lbg/blob/master/lbg.py
% https://github.com/aashishkr/Image-Compression-Using-Vector-Quantization-with-LBG-algorithm

%% data preparation

path = 'C:\Users\fosca\Documents\UNIPD\Magistrale_ICT\Multimedia_Coding\project_repo\MCoding_project\data\';
% path = 'C:\Users\fosca\Documents\UNIPD\Magistrale_ICT\Multimedia_Coding\project_repo\MCoding_project\Data_Set\Images\';
A = imread(strcat(path,'lena.tiff'));
imshow(A)

%% Try image with good ol' kmeans first
%reshape image stacking columns
k = 3
A_r = reshape(A, [],3);
idx = kmeans(double(A_r), k);
A_k = reshape(idx, 512, 512,1);
A_k = uint8(A_k * 255 / k);

imshow(A_k)
%%

