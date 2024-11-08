% Specify the desired size of the resized images
targetSize = [64, 64];

% Specify the folder containing the GIF frames
folderPath = 'frames1';

% Specify the number of times to copy each image for noisy versions
numCopies = 20;

% Specify the standard deviation of the Gaussian noise
noiseStdDev = 0.1;

% Get a list of all the image files in the folder
fileList = dir(fullfile(folderPath, '*.png'));

% Create folders for saving ground truth and noisy images
groundTruthPath = 'groundtruth/';
noisyImagePath = 'gray1/';

% Create folders for saving ground truth and noisy images if they don't exist
if ~exist(groundTruthPath, 'dir')
    mkdir(groundTruthPath);
end
if ~exist(noisyImagePath, 'dir')
    mkdir(noisyImagePath);
end

% Process only 14 images (assuming each GIF provides a frame for ground truth)
numGroundTruth = min(14, numel(fileList));
for i = 1:numGroundTruth
    % Read the current image file
    fileName = fullfile(folderPath, fileList(i).name);
    imgData = imread(fileName);

    % Resize the image to the target size
    resizedImage = imresize(imgData, targetSize);

    % Convert the resized image to grayscale
    grayImage = im2gray(resizedImage);

    % Save the grayscale image as the ground truth image
    groundTruthFileName = fullfile(groundTruthPath, [num2str(i), '.png']);
    imwrite(grayImage, groundTruthFileName);

    % Generate and save noisy copies of the ground truth image
    for k = 1:numCopies
        % Add Gaussian noise to the ground truth image
        noisyImage = imnoise(grayImage, 'gaussian', 0, noiseStdDev^2);

        % Save each noisy image with a unique name
        noisyFileName = fullfile(noisyImagePath, [num2str((i-1)*numCopies + k), '.png']);
        imwrite(noisyImage, noisyFileName);
    end
end