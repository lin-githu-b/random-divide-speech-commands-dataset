import os
import random
import scipy.io.wavfile as wav


def save_to_target_dirs(root, save_dataset_root, train_files,
                        validation_files, test_files, dataset_root_start=0):

    for scope in ['train', 'validation', 'test']:
        save_data_path = os.path.join(save_dataset_root, scope)

        for i in root.split('/')[dataset_root_start:]:
            save_data_path = os.path.join(save_data_path, i)

        if save_data_path:
            if not os.path.exists(save_data_path):
                os.makedirs(save_data_path)

        if scope == 'train':
            x_files = train_files
        else:
            if scope == 'validation':
                x_files = validation_files
            else:
                x_files = test_files
        for file in x_files:
            file_path = os.path.join(root, file)
            save_file_path = os.path.join(save_data_path, file)
            fs, data = wav.read(file_path)
            wav.write(save_file_path, rate=fs, data=data)


def random_divide_dataset(dataset_path, save_dataset_root, train_rate=0.6, validation_rate=0.2):
    for root, dirs, files in os.walk(dataset_path):

        if len(files) <= 10:
            continue

        start = len(dataset_path.split('/'))

        train_files = random.sample(files, int(len(files) * train_rate))
        residue_files = [item for item in files if item not in train_files]
        validation_files = random.sample(residue_files, int(len(files) * validation_rate))
        test_files = [item for item in residue_files if item not in validation_files]

        print("what command is it now:", root.split('/')[-1])
        print("length of train:", len(train_files))
        print("length of validation:", len(validation_files))
        print("length of test:", len(test_files))

        save_to_target_dirs(root, save_dataset_root, train_files, validation_files,
                            test_files, start)

        '''
        for scope in ['train', 'validation', 'test']:
            save_data_path = os.path.join(save_dataset_root, scope)

            for i in root.split('/')[start:]:
                save_data_path = os.path.join(save_data_path, i)

            if save_data_path:
                if not os.path.exists(save_data_path):
                    os.makedirs(save_data_path)

            if scope == 'train':
                x_files = train_files
            else:
                if scope == 'validation':
                    x_files = validation_files
                else:
                    x_files = test_files
            for file in x_files:
                file_path = os.path.join(root, file)
                save_file_path = os.path.join(save_data_path, file)
                fs, data = wav.read(file_path)
                wav.write(save_file_path, rate=fs, data=data)
        
        '''



if __name__=="__main__":
    dataset_path = "/media/lin/data/speech_commands"
    save_dataset_root = "/media/lin/data/speech_commands_random_divided"
    train_rate = 0.6
    validation_rate = 0.2
    random_divide_dataset(dataset_path,
                          save_dataset_root,
                          train_rate=train_rate,
                          validation_rate=validation_rate)