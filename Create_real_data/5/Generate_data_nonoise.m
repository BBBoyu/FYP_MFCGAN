% Specify the desired size of the resized images
targetSize = [64, 64];

% Specify the folder containing the GIF files
folderPath = 'frames';

% Specify the number of times to copy each image
numCopies = 20;

% Get a list of all the PNG files in the folder
fileList = dir(fullfile(folderPath, '*.png'));

% Process each PNG file
for i = 1:numel(fileList)
    % Read the current PNG file
    fileName = fullfile(folderPath, fileList(i).name);
    imageData = imread(fileName);

    % Resize image to the target size
    resizedImage = imresize(imageData, targetSize);

    % Convert resized image to grayscale if it is in color
    if size(resizedImage, 3) == 3
        grayImage = rgb2gray(resizedImage);
    else
        grayImage = resizedImage;
    end

    % Copy the grayscale image 20 times
    copiedImages = cell(1, numCopies);
    for k = 1:numCopies
        copiedImages{k} = grayImage;
    end

    % Save the copied images as PNG with sequential names
    savepath = 'gray1/';
    for j = 1:numCopies
        saveFileName = fullfile(savepath, [num2str((i-1)*numCopies + j), '.png']);
        imwrite(copiedImages{j}, saveFileName);
    end
end
