import configargparse
import argparse


def get_twins_args():    
    parser = configargparse.ArgParser(config_file_parser_class=configargparse.YAMLConfigFileParser)
    parser.add_argument("--mixed_precision", type=str, default=True)
    parser.add_argument("--small", type=str, default=False)
    parser.add_argument("--iters", type=int, default=12)
    parser.add_argument("--dim_corr", type=int, default=192)
    parser.add_argument("--dim_corr_coarse", type=int, default=64)
    parser.add_argument("--dim_corr_all", type=int, default=192)    
    parser.add_argument("--model", type=str, default="./pretrained_models/twins_one.pth")
    parser.add_argument("--fnet", type=str, default='twins')
    parser.add_argument("--twoscale", type=str, default=False)
    return parser.parse_known_args()[0]    


def get_life_args():
    parser = configargparse.ArgParser(config_file_parser_class=configargparse.YAMLConfigFileParser)
    parser.add_argument('--iters', type=int, default=12)
    parser.add_argument('--mixed_precision', type=bool, default=True)
    parser.add_argument('--small', action='store_true', help='use small model')
    parser.add_argument("--fnet", type=str, default='CNN')
    parser.add_argument('--model', type=str, default="./pretrained_models/cnn_one.pth", help="choose the trained model")    
    args = parser.parse_known_args()[0]
    return args


def get_video_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--demo_root', type=str, default='./demo/demo_video/')
    parser.add_argument('--scene_name', type=str, default='scene.mp4')
    parser.add_argument('--marker_name', type=str, default='fantastic_beast.jpg')
    parser.add_argument('--movie_name', type=str, default='movie.mp4')
    parser.add_argument('--save_name', type=str, default='out.avi')
    parser.add_argument('--movie_start_idx', type=int, default=0)
    parser.add_argument('--scene_start_idx', type=int, default=150)        

    parser.add_argument('--test', action='store_true', help='test specified scene and frame')
    parser.add_argument('--scene_id', type=int, default=0)
    parser.add_argument('--frame_id', type=int, default=0)
    parser.add_argument('--draw', action='store_true')
    parser.add_argument('--save', action='store_true')
    
    return parser.parse_args()

def get_harsh_lighting_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--exp_dir', type=str, default='./demo/demo_harsh_lighting')
    parser.add_argument('--marker_name', type=str, default='fantastic_beast.jpg')
    parser.add_argument('--scene_name', type=str, default='scene_beast.jpg')        
    parser.add_argument('--source_name', type=str, default='doctor_strange.jpg')
    parser.add_argument('--poster_brightness', type=float, default=1/4.5)    
    parser.add_argument('--model', type=str, default='twins-onestage')
    parser.add_argument('--save_decomposed', action='store_true', help='save scene image decomposition results or not')
    return parser.parse_args()