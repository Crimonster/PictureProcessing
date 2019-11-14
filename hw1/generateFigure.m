function[img] = generateFigure(imgH,imgW)
% 初始化
img = zeros(imgH,imgW,3);
img = uint8(img);
% 设置背景为白色
for i=1:3
  img(:,:,i)=255;
% 生成x在[0,2*pi]数据ff
x=0:2*pi/(imgW-1):2*pi;
% 计算相应的y
red=sin(x);
green=cos(x);
blue=x.^2;
% 把x映射到图片上
img_x = uint16(x/2/pi*imgW);
% 把y映射到图片上 
img_red = uint16(imgH/30*25-round(red*imgH/30));
img_green = uint16(imgH/30*25-round(green*imgH/30));
img_blue = uint16(imgH/30*25-round(blue*imgH/30));
% 从左到右画图
for i=1:imgW
    if img_x(i)==0
        img_x(i)=img_x(i)+1;
    end
    if img_red(i)>0 && img_red(i)<=imgH
        img(img_red(i),img_x(i),2)=0;
        img(img_red(i),img_x(i),3)=0;
    end
    if img_green(i)>0 && img_green(i)<=imgH
        img(img_green(i),img_x(i),3)=0;
        img(img_green(i),img_x(i),1)=0;
    end
    if img_blue(i)>0 && img_blue(i)<=imgH
        img(img_blue(i),img_x(i),1)=0;
        img(img_blue(i),img_x(i),2)=0;
    end
end

% 坐标轴
img(:,1,:)=0;
img(imgH/30*25,:,:)=0;
imshow(img);
end

