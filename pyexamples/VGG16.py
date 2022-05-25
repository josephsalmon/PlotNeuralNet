
import sys
sys.path.append('../')
from pycore.tikzeng import *  # noqa: E402
from pycore.blocks import *  # noqa: E402

# uses: https://github.com/HarisIqbal88/PlotNeuralNet/issues/52

arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    # inputmy_project
    # to_input('../examples/fcn8s/cats.jpg'),
    # Pl@ntnet image: 1355936,Cirsium arvense,Cirsium,3418,12075

    to_input('cf7315479b5bebc714b824045f729868d8b6ca73.jpg'),
    # to_input('d80a7c1334c62039e8c9b6d0b98256c16c0de30e.jpg'),

    # conv1
    to_ConvConvRelu(name='cr1', s_filer=224, n_filer=(64, 64), offset="(0.3,0,0)",
                    to="(0,0,0)", width=(2, 2), height=40, depth=40, caption="conv1"),
    to_Pool(name="p1", offset="(0.2,0,0)", to="(cr1-east)",
            width=2, height=20, depth=20, opacity=0.5),

    # conv2
    to_ConvConvRelu(name='cr2', s_filer=112, n_filer=(128, 128), offset="(2.5,0,0)",
                    to="(p1-east)", width=(3, 3), height=20, depth=20, caption="conv2"),
    to_Pool(name="p2", offset="(0,0,0)", to="(cr2-east)",
            width=3, height=10, depth=10, opacity=0.5),

    # conv3
    to_ConvConvRelu(name='cr3', s_filer=56, n_filer=("256", "256", "256"), offset="(1.5,0,0)",
                    to="(p2-east)", width=(4, 4, 4), height=10, depth=10, caption="conv3"),
    to_Pool(name="p3", offset="(0,0,0)", to="(cr3-east)",
            width=4, height=5, depth=5, opacity=0.5),

    # conv4
    to_ConvConvRelu(name='cr4', s_filer=28, n_filer=("512", "512", "512"), offset="(1.2,0,0)",
                    to="(p3-east)", width=(5, 5, 5), height=5, depth=5, caption="conv4"),
    to_Pool(name="p4", offset="(0,0,0)", to="(cr4-east)",
            width=5, height=2.5, depth=2.5, opacity=0.5),

    # conv5
    to_ConvConvRelu(name='cr5', s_filer=14, n_filer=("512", "512", "512"), offset="(1,0,0)",
                    to="(p4-east)", width=(6, 6, 6), height=2.5, depth=2.5, caption="conv5"),
    to_Pool(name="p5", offset="(0,0,0)", to="(cr5-east)",
            width=6, height=1.25, depth=1.25, opacity=0.5),

    # flatten
    to_FullyConnected(name="fl", s_filer=4096, offset="(2.0,0,0)",
                      to="(p5-east)", width=1, height=1, depth=40, caption="fc1\ndr"),

    # fc1
    to_FullyConnected(name="fc1", s_filer=4096, offset="(1.25,0,0)",
                      to="(fl-east)", width=1, height=1, depth=40, caption="fc2\ndr"),

    # fc2
    # to_FullyConnected(name="fc2", s_filer=4096, offset="(1.25,0,0)",
    #                   to="(fc1-east)", width=1, height=1, depth=40, caption="fc2\ndr"),

    # fc3
    to_FullyConnected(name="fc3", s_filer="L", offset="(1.25,0,0)",
                      to="(fc1-east)", width=1, height=1, depth=15, caption="fc3\ndr"),


    # sigmoid
    to_SoftMax(name="sg", s_filer="L", n_filer="", offset="(1.25,0,0)", to="(fc3-east)",
               width=1, height=1, depth=15, caption="SIGMOID", opacity=1.0),

    # connections
    to_connection("p1", "cr2"),
    to_connection("p2", "cr3"),
    to_connection("p3", "cr4"),
    to_connection("p4", "cr5"),
    to_connection("p5", "fl"),
    to_connection("fl", "fc1"),
    to_connection("fc1", "fc3"),
    # to_connection("fc2", "fc3"),
    to_connection("fc3", "sg"),
    to_connection("sg", "++(1.5,0,0)", to_dir=''),

    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
