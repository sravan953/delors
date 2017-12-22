% Author - Pavan Poojar
% Modified by - Keerthi Sravan Ravi
% Date - 21/12/2017

function IterAddPhase(folder_name)
    % Pwd to cd back into at the end
    present_folder = pwd;

    % Parent directory containing the images
    root_path = '/Users/sravan953/Documents/MIRC/Projects/Delors/Data/64/imagenet_64/';
    src_path = strcat(root_path, folder_name);
    cd(src_path);
    mkdir(strcat(root_path, 'mat_output/', folder_name));

    % Most times, these unnecessary items have to be removed:
    % ('.', '..', '.DS_store') 
    files = dir(pwd);
    files('.') = [];
    files('..') = [];
    files('.DS_store') = [];
    k = zeros(length(files)-1, 1);

    for i=1:length(k-1)
        try
            I = double(imread(num2str(i), 'jpg'));
            I1= edge(I,'sobel'); % edge detection
            I2=I-I1;

            I2 = I2 - min(I2(:))./(max(I2(:)) - min(I2(:))); % in the range 0 to 1
            I2 = I2 - 0.5;                                   % in the range -0.5 to + 0.5
            I3 = I2.*2*pi;

            I4_r = I.*cos(I3);
            I4_i = I.*sin(I3);
            I4 = complex(I4_r, I4_i);

            k=fftshift(fft2(I4));

            % Save variable k as a mat file at specified location
            save(strcat(root_path, 'mat_output/', folder_name, '/', num2str(i), '.mat'), 'k');
        catch error
            disp(error);
        end
    end
    cd(present_folder);
end