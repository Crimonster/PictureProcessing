function[]=bin(mag)
% magnification
img = imread('1.jpg');
% zi-oi, mag-mag
[IH,IW,ID] = size(img);
OIH = round(IH*mag); % �������ź��ͼ��߶ȣ����ȡ��
OIW = round(IW*mag); % �������ź��ͼ���ȣ����ȡ��
OI = zeros(OIH,OIW,ID); % ������ͼ��
% ��չ����I��Ե
IT = zeros(IH+2,IW+2,ID);
IT(2:IH+1,2:IW+1,:) = img;
IT(1,2:IW+1,:)=img(1,:,:);IT(IH+2,2:IW+1,:)=img(IH,:,:);
IT(2:IH+1,1,:)=img(:,1,:);IT(2:IH+1,IW+2,:)=img(:,IW,:);
IT(1,1,:) = img(1,1,:);IT(1,IW+2,:) = img(1,IW,:);
IT(IH+2,1,:) = img(IH,1,:);IT(IH+2,IW+2,:) = img(IH,IW,:);

% Step4 ����ͼ���ĳ�����أ�zi��zj��ӳ�䵽ԭʼͼ��(ii��jj)��������ֵ��
for zj = 1:OIW         % ��ͼ����а�����Ԫ��ɨ��
    for zi = 1:OIH
        ii = (zi-1)/mag; jj = (zj-1)/mag;
        i = floor(ii); j = floor(jj); % ����ȡ��
        u = ii - i; v = jj - j;
        i = i + 1; j = j + 1;
        OI(zi,zj,:) = (1-u)*(1-v)*IT(i,j,:) +(1-u)*v*IT(i,j+1,:)...
                    + u*(1-v)*IT(i+1,j,:) +u*v*IT(i+1,j+1,:);
    end
end
imshow(uint8(OI));

