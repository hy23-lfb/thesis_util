function plot_result_difference(filepath1, filepath2, strpath)

warning('off','MATLAB:MKDIR:DirectoryExists');

anyFilePath = filepath1; % can be filepath2 also.

mkdir(strpath);

dir_list = dir(anyFilePath);
len_dir  = length(dir_list);

% first two entries are "." and ".." so let's ignore it.
for dirIdx = 3:len_dir
    fname = dir_list(dirIdx).name;
    file = fullfile(anyFilePath, fname);
    if(endsWith(file, '.tif'))
        file1 = fullfile(filepath1, fname);
        file2 = fullfile(filepath2, fname);

        f1 = imread(file1);
        f2 = imread(file2);

        f = figure('units','normalized','outerposition',[0 0 1 1]);
        subplot(1,3,1);
        imshow(f1);

        subplot(1,3,2);
        imshow(f2);

        subplot(1,3,3)
        imshowpair(f1, f2);

        saveFile = fullfile(strpath, fname);
        saveas(f, saveFile);

        close all;
    else
            % any other file
    end
end

end