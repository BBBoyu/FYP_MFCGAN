% Define paths
input_folder = 'noisy_images_4';
output_folder = 'denoised_images';
if ~exist(output_folder, 'dir')
    mkdir(output_folder);
end

% Process each image in the folder
image_files = dir(fullfile(input_folder, '*.png'));
for i = 1:length(image_files)
    % Load each noisy image
    noisy_img = imread(fullfile(input_folder, image_files(i).name));
    
    % Convert to grayscale if needed
    if size(noisy_img, 3) == 3
        noisy_img = rgb2gray(noisy_img);
    end
    
    % Denoise the image
    net = denoisingNetwork("DnCNN");
    denoised_img = denoiseImage(noisy_img, net);
    
    % Save the denoised image
    output_name = fullfile(output_folder, image_files(i).name);
    imwrite(denoised_img, output_name);
    fprintf('Denoised image saved: %s\n', output_name);
end