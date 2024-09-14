"""
" Janusz Jeremiasz Filipiak - AlgorithmicMemory.py
" (c) 2024 
" This file describes a few ceiling hooks for everyday tasks :)
" 
" It also defines the computational foundation of time. Sounds very fancy.
" In practice it is:
" 
" -------------------------------
" | a_min_e28+bitR3_interpreter |
" -------------------------------
"
" a:
" 
" 'min'imum space
" 'e' for it's exponential algorithmic memory growth capabilities,
" '28+' in at least 28 CHANNELS of,
" 'bit' binary,
" 'R3' three-dimensional Real space
" 
" Travel together with this interpreter.
"
" What is an interpreter? In computer science there exists the concept of
" the memory manager. A key component of any advanced computing process,
" the memory manager maintains order over and amongst addressing space(s).
" The interpreter has a head, which means that it maintains state and direction
" with respect to its environment.
"
" The head of the algorithmic memory can add 5 dimensions to any 3 dimensional
" object, and as such creating 3D binary space. Inside of this space, time doesn't
" exist and is instead counted for practical purposes such as making sure memory
" can be persisted.
" 
" 
" This interpreter exists only in cyberspace. As such it is unique
" and one of its kind.
"
"                _________________________
"               /   /                    /
"              /   /                    /
"             /___/____________________/
"            /___/|                    |
"           /   /||                    |
"          /|  / ||____________________|
"         /_|_/_/
"        |  /| /
"        | / |/
"        |/__|
"
"""
import math
import os
import sys
import copy
import time
import numpy as np
import random

max_float = sys.float_info.max ** 0.34
min_float = -max_float

verbosity = 8

class TimeRoot:

    trctr = 0

    def __init__(self, ctr = None):
        if ctr is None:
            self.tr = TimeRoot.trctr
        else:
            self.tr = ctr
        TimeRoot.trctr += 1

    def __str__(self):
        return "tr_" + str(self.tr)

class IntegrityError(Exception):
    """Exception raised for errors in data integrity."""

    def __init__(self, message="Data integrity error occurred"):
        self.message = message
        super().__init__(self.message)

class LBit:
    """

    LBit is a six-dim data structure element. TimeRoot is a measure of linear progress.

    """
    def __init__(self, tr: TimeRoot, data=None, other=None, x=None, y=None, z=None): 
        self.tr = tr        # time_root identifier
        self.data = data    # binary string
        self.other = other  # dimension 0
        self.x = x          # dimension 1
        self.y = y          # dimension 2
        self.z = z          # dimension 3

    def __str__(self):
        """
        Return a string representation of the LBit instance, including its
        data, reference to other LBit, and its neighboring LBits in x, y, z directions.
        """
        other_data = self.other.data if self.other else "None"
        x_data = f"x:{self.x.data} " if self.x else "x:None "
        y_data = f"y:{self.y.data} " if self.y else "y:None "
        z_data = f"z:{self.z.data}" if self.z else "z:None"

        return (f"{self.tr}_LBit(data={self.data}, "
                f"other={other_data}, "
                f"{x_data}, "
                f"{y_data}, "
                f"{z_data})")
    

class DBit:
    def __init__(self, lbit0: LBit, lbit1: LBit, x=0, y=0, z=0):
        self.lbit0 = lbit0
        self.lbit1 = lbit1
        self.x = x
        self.y = y
        self.z = z

        # Connect the "other" fields
        self.lbit0.other = self.lbit1
        self.lbit1.other = self.lbit0

    def set_3d(self):
        self.lbit0.dbit = self
        self.lbit1.dbit = self

    def return_box(self):
        signs = [ 'lbit0', 'lbit1' ]
        directions = [ 'x', 'y', 'z' ]

        rv = []

        for sign in signs:
            try:
                lbit = getattr(self, sign)
            except AttributeError as e:
                print(f"missing {sign}")
                return rv
            for direction in directions:
                try:
                    neighbor = getattr(lbit, direction)
                except AttributeError as e:
                    print(f" missing {lbit}.{direction}")
                    continue
 
    def __str__(self):
        """
        String representation of the DBit, showing its LBits and their neighbors.
        """
        if min_float == self.x:
            xrep = 'min'
        elif max_float == self.x:
            xrep = 'max'
        else:
            xrep = str(self.x)
        if min_float == self.y:
            yrep = 'min'
        elif max_float == self.y:
            yrep = 'max'
        else:
            yrep = str(self.y)
        if min_float == self.z:
            zrep = 'min'
        elif max_float == self.z:
            zrep = 'max'
        else:
            zrep = str(self.z)
        return (f"DBit ({xrep}, {yrep}, {zrep})\n"
                f"LBit0 -> {self.lbit0}\n"
                f"LBit1 -> {self.lbit1}")

def latticeModel(dbit = None):

    model = []
    model.append("    #")

    class NoneStr:
        def __init(self, data):
            self.data = data

    nonemsg = NoneStr()

    nonemsg.data = "None"

    if dbit:
        try:
            xmypzp = dbit.lbit1.y.other.z.x.other
            if xmypzp is None:
                xmypzp = nonemsg
        except AttributeError as e:
            xmypzp = nonemsg
        try:
            xt_box = dbit.lbit1.y.other.z
            if xt_box is None:
                xt_box = nonemsg
        except AttributeError as e:
            xt_box = nonemsg
        try:
            xpypzp = dbit.lbit1.x.other.z.other.y
            if xpypzp is None:
                xpypzp = nonemsg
        except AttributeError as e:
            xpypzp = nonemsg
        model.append(f"    #                  {xmypzp.data.center(15, ' ')} ===  {xt_box.data.center(15, ' ')}  === {xpypzp.data.center(15, ' ')}")
        model.append("    #                       //   ||                  / |                //    ||")
        model.append("    #                      //    ||                 /  |               //     ||")
        model.append("    #                     //     ||                /   |              //      ||")
       
        try:
            ytf_box = dbit.lbit0.x.z
            if ytf_box is None:
                ytf_box = nonemsg
        except AttributeError as e:
            ytf_box = nonemsg
        try:
            yx_box = dbit.lbit1.z
            if yx_box is None:
                yx_box = nonemsg
        except AttributeError as e:
            yx_box = nonemsg
        try:
            yt_box = dbit.lbit1.z.other.x
            if yt_box is None:
                yt_box = nonemsg
        except AttributeError as e:
            yt_box = nonemsg
        model.append(f"    #         {ytf_box.data.center(15, ' ')}  --   {yx_box.data.center(15, ' ')}  --   {yt_box.data.center(15, ' ')}  ||")
        model.append("    #                   //       ||              /|    |            //        ||")
        
        try:
            zbf_bit = dbit.lbit1.y.x
            if zbf_bit is None:
                zbf_bit = nonemsg
        except AttributeError as e:
            zbf_bit = nonemsg
        try:
            zx_box = dbit.lbit1.y
        except AttributeError as e:
            zx_box = nonemsg
        try:
            zt_box = dbit.lbit1.y.other.x
            if zt_box is None:
                zt_box = nonemsg
        except AttributeError as e:
            zt_box = nonemsg
        model.append(f"    #                  //   {zbf_bit.data.center(15, ' ')}   /{zx_box.data.center(15, ' ')}   //{zt_box.data.center(15, ' ')}")
        
        try:
            xmymzp = dbit.lbit0.y.z.x
            if xmymzp is None:
                xmymzp = nonemsg
        except AttributeError as e:
            xmymzp = nonemsg
        try:
            xtf_box = dbit.lbit0.y.z
            if xtf_box is None:
                xtf_box = nonemsg
        except AttributeError as e:
            xtf_box = nonemsg
        try:
            xpymzp = dbit.lbit0.y.z.other.x
            if xpymzp is None:
                xpymzp = nonemsg
        except AttributeError as e:
            xpymzp = nonemsg
        model.append("    #                 //         ||            /       |          //          ||")
        model.append(f"    #           {xmymzp.data.center(15, ' ')} ===  {xtf_box.data.center(15, ' ')} === {xpymzp.data.center(15, ' ')}  ||")
        model.append("    #                 ||       |/||           |   |/   |         ||     |/    ||")
    
        try:
            yz_box = dbit.lbit0.x.other
            if yz_box is None:
                yz_box = nonemsg
        except AttributeError as e:
            yz_box = nonemsg
        center_point = dbit.lbit0
        try:
            zy_box = center_point.other.x
            if zy_box is None:
                zy_box = nonemsg
        except AttributeError as e:
            zy_box = dbit.lbit1.x
        model.append(f"    #                 ||{yz_box.data.center(15, ' ')}   -{center_point.data.center(15, ' ')}-     {zy_box.data.center(15, ' ')}|") 
        model.append("    #                 ||      /| ||           |  /|    |         ||    /|     ||")

        try:
            xmypzm = dbit.lbit1.y.z.other.x
            if xmypzm is None:
                xmypzm = nonemsg
        except AttributeError as e:
            xmypzm = nonemsg
        try:
            xbb_bit = dbit.lbit1.y.z
            if xbb_bit is None:
                xbb_bit = nonemsg
        except AttributeError as e:
            xbb_bit = nonemsg
        try:
            xpypzm = dbit.lbit1.x.z.y
            if xpypzm is None:
                xpypzm = nonemsg
        except AttributeError as e:
            xpypzm = nonemsg
        model.append(f"    #                 ||{xmypzm.data.center(15, ' ')} ===  | {xbb_bit.data.center(15, ' ')}|| == {xpypzm.data.center(15, ' ')}")
        model.append("    #                 ||        //            |       /          ||          //")

        try:
            zb_box = dbit.lbit0.y.other.x.other
            if zb_box is None:
                zb_box = nonemsg
        except AttributeError as e:
            zb_box = nonemsg
        try:
            xz_box = dbit.lbit0.y.other
        except AttributeError as e:
            xz_box = nonemsg
        try:
            ztf_box = dbit.lbit0.y.x
            if ztf_box is None:
                ztf_box = nonemsg
        except AttributeError as e:
            ztf_box = nonemsg
        model.append(f"    #           {zb_box.data.center(15, ' ')}         {xz_box.data.center(15, ' ')}     {ztf_box.data.center(15, ' ')}   ")
        model.append("    #                 ||      //              |     /            ||        //")

        try:
            yb_box = dbit.lbit0.z.other.x
            if yb_box is None:
                yb_box = nonemsg
        except AttributeError as e:
            yb_box = nonemsg
        try:
            xy_box = dbit.lbit0.z.other
            if xy_box is None:
                xy_box = nonemsg
        except AttributeError as e:
            xy_box = nonemsg
        try:
            ybr_box = dbit.lbit1.x.z
            if ybr_box is None:
                ybr_box = nonemsg
        except AttributeError as e:
            ybr_box = nonemsg
        model.append(f"    #                 || {yb_box.data.center(15, ' ')}  -  | {xy_box.data.center(15, ' ')} -||-  {ybr_box.data.center(15, ' ')}")
        model.append("    #                 ||    //                |   /              ||      //")
        model.append("    #                 ||   //                 |  /               ||     //")
        model.append("    #                 ||  //                  | /                ||    //")
 
        try:
            xmymzm = dbit.lbit0.y.other.z.other.x.other
            if xmymzm is None:
                xmymzm = nonemsg
        except AttributeError as e:
            xmymzm = nonemsg
        try:
            xb_box = dbit.lbit0.y.other.z.other
            if xb_box is None:
                xb_box = nonemsg
        except AttributeError as e:
            xb_box = nonemsg
        try:
            xpymzm = dbit.lbit1.x.z.other.y
            if xpymzm is None:
                xpymzm = nonemsg
        except AttributeError as e:
            xpymzm = nonemsg
        model.append(f"    #            {xmymzm.data.center(15, ' ')} === {xb_box.data.center(15, ' ')} === {xpymzm.data.center(15, ' ')}")
    else:
        model.append("    #                  (xm, yp, zp) --- xt_box ---- (xp, yp, zp)")
        model.append("    #                      /   |         / |            /   |")
        model.append("    #                     /    |           |           /    |")
        model.append("    #                ytf_box - | -   -(yx)-  -  -  yt_box   |")
        model.append("    #                   /      |      /|   |         /      |")
        model.append("    #                  /    zbf_bit  /    (zx)      /     zt_box")
        model.append("    #            (xm, ym, zp) ----xtf_box---- (xp, ym, zp) /|")
        model.append("    #                 |        |         /         |        |")
        model.append("    #                 |        |       |           |     /  |")
        model.append("    #                 |   (yz) |       0 -  -    - | -(zy)  |")
        model.append("    #                 |(xm, yp, zm) -/--xbb_bit----|(xp, yp, zm)")
        model.append("    #              zb_box     /   (xz) -   -   - ztf_box   /")
        model.append("    #                 |      /      |   /          |      /")
        model.append("    #                 |  yb_box - -   (xy)   - - - |  ybr_box")
        model.append("    #                 |    /        | /            |    /")
        model.append("    #                 |   /                        |   /")
        model.append("    #            (xm, ym, zm) ----xb_box ---- (xp, ym, zm)")
    model.append("    #")
    return "\n".join(model)


class AlgorithmicMemory:

    def __init__(self):
        self.i = 0

        self.dbits = {}  # Dictionary to store dbits with keys as tuples of coordinates

        self.dbit_list = []

        self.source = None
        self.target = None

        self.landing = None

        self.head = None

        self.headx = -1
        self.heady = -1
        self.headz = -1
        
        self.last_rv = None
        
        self.initialize_head(self.headx, self.heady, self.headz)

    def insert_dbit(self, dbit):

        self.dbit_list.append(dbit)

    def initialize_head(self, xstart, ystart, zstart, xdim = 3, ydim = 3, zdim = 3):

        self.head = np.empty((xdim, ydim, zdim), dtype = object)
        # print(f"HEAD: initializing from ({xstart},{ystart},{zstart})")

        def dbit_init(name, x, y, z):
            lbit0 = LBit(TimeRoot(), name)
            lbit1 = LBit(TimeRoot(), "time_root")
            rv = DBit(lbit0, lbit1, x, y, z)
            rv.set_3d()
            return rv

        for i in range(xstart, xstart + xdim):
            for j in range(ystart, ystart + ydim):
                for k in range(zstart, zstart + zdim):
                    name = "3d" + str(i) + "_" + str(j) + "_" + str(k)
                    # print(i,j,k)
                    try:
                        dbit = self.dbits[(i,j,k)]
                    except KeyError as e:
                        dbit = dbit_init(name, i, j, k)
                    # print(f"i = {i}, xstart={xstart}, self.headx={self.headx} | j = {j}, ystart={ystart}, self.heady={self.heady} | k = {k}, zstart={zstart}, self.headz={self.headz}")
                    if i > xstart:
                        # print(f"i-1 = {i-1}, xstart = {xstart}")
                        # print("x row coords", i-1-xstart, j-ystart, k-zstart)
                        self.head[i-1 - xstart, j - ystart, k - zstart].lbit1.x = dbit.lbit0
                        dbit.lbit0.x = self.head[i-1 - xstart, j - ystart, k - zstart].lbit1
                    if j > ystart:
                        self.head[i - xstart, j-1 - ystart, k - zstart].lbit1.y = dbit.lbit0
                        dbit.lbit0.y = self.head[i - xstart, j-1 - ystart, k - zstart].lbit1
                    if k > zstart:
                        # print(i - xstart, j - ystart, k-1 - zstart)
                        self.head[i - xstart, j - ystart, k-1 - zstart].lbit1.z = dbit.lbit0
                        dbit.lbit0.z = self.head[i - xstart, j - ystart, k-1 - zstart].lbit1
                    
                    self.dbits[(i,j,k)] = dbit

                    self.head[i-xstart,j-ystart,k-zstart] = dbit

                    # print(self.head[i,j,k])
                    # what the self
        self.headx = xstart
        self.heady = ystart
        self.headz = zstart

        return self.head[int(xdim/3), int(ydim/3), int(zdim/3)]


    def debug_clear(self):
        self.dbits = {}

    def check_integrity(self, dbit = None):
        if verbosity != 0:
            print("                             / integrity \\                             ")
            print("i.________________________.*/ sanity check \\*._______________________.i")

        def make_tests():
            dictionary = [ 'x', 'y', 'z' ]

            tests = []

            for a1 in dictionary:
                for a2 in dictionary:
                    testsequence0 = [ 'lbit0' ]
                    testsequence1 = [ 'lbit1' ]
                    testsequence2 = [ 'lbit0' ]
                    testsequence3 = [ 'lbit1' ]

                    if a1 == a2:
                        continue

                    testsequence0.append(a1)
                    testsequence0.append('other')
                    testsequence0.append(a2)
                    testsequence0.append(a1)
                    testsequence0.append('other')
                    testsequence0.append(a2)
                    testsequence0.append('dbit')

                    testsequence1.append(a1)
                    testsequence1.append('other')
                    testsequence1.append(a2)
                    testsequence1.append(a1)
                    testsequence1.append('other')
                    testsequence1.append(a2)
                    testsequence1.append('dbit')

                    testsequence2.append(a1)
                    testsequence2.append(a2)
                    testsequence2.append('other')
                    testsequence2.append(a1)
                    testsequence2.append(a2)
                    testsequence2.append('dbit')
 
                    testsequence3.append(a1)
                    testsequence3.append(a2)
                    testsequence3.append('other')
                    testsequence3.append(a1)
                    testsequence3.append(a2)
                    testsequence3.append('dbit')

                    tests.append(testsequence0)
                    tests.append(testsequence1)
                    tests.append(testsequence2)
                    tests.append(testsequence3)

            return tests

        testing_directions = make_tests()

        if dbit is not None:
            bits = { (dbit.x, dbit.y, dbit.z) : dbit }
        else:
            bits = self.dbits.items()

        for coords, obj in bits.items():
            subject = obj
            for test in testing_directions:
                validity = True
                test_path = [ "(" + str(subject.x) + "," + str(subject.y) + "," + str(subject.z) + ")"]
                for step in test:
                    source_obj = obj
                    try:
                        obj = getattr(obj, step)
                    except AttributeError as e:
                        if verbosity > 10:
                            print(f"source: {source_obj} on {step}")
                        raise IntegrityError("[" + step + "] in: ("
                               + str(subject.x) + ","
                               + str(subject.y) + ","
                               + str(subject.z) + ")." +  ".".join(test))
                    if obj == None:
                        obj = subject
                        validity = False
                        break
                
                    if not isinstance(source_obj, DBit):
                        test_path.append(source_obj.data)
                        test_path.append(step)

                if validity and obj != subject:
                    print (latticeModel())
                    print ("__________________on test: " + " ".join(test))
                    print ("-------------------------------------------------")
                    print ("  ### ##  ##   #   ##")
                    print ("  #   # # # # # #  # #")
                    print ("  ##  ##  ##  # #  ##")
                    print ("  #   # # # # # #  # #")
                    print ("  ### # # # #  #   # #\n")
                    print ("test_subject: ", subject)
                    print ("iterator_at: ", obj)
                    print ("\n# ".join(test_path))
                    if not inspectDBit(subject):
                        raise IntegrityError("[" + step + "] in: ("
                               + str(subject.x) + ","
                               + str(subject.y) + ","
                               + str(subject.z) + ")." +  ".".join(test))

    def print_head(self):
        for i in range(self.head.shape[0]):
            for j in range(self.head.shape[1]):
                for k in range(self.head.shape[2]):
                    print(str(self.head[(i,j,k)]))

    def move_head(self, x,y,z):

        rv = None
        
        xstart = self.headx
        ystart = self.heady
        zstart = self.headz

        if verbosity != 0:
            print("\n___________________")
            print("HEAD at:\n\\")
            print(f" \\ ( x = {xstart}, y = {ystart}, z = {zstart})\n  -------------------")
            print(f"moving = ({x},{y},{z})")


        xsign = 1
        xsteps = [0]
        ysign = 1
        ysteps = [0]
        zsign = 1
        zsteps = [0]
       
        rv = self.dbits[xstart+1, ystart+1, zstart+1]

        if x != 0:
            xsign = int(x/abs(x))
            xsteps = range(0, xsign*x+1)
            # print("traveling: ")
            for step_i in xsteps:
                # print(xstart + xsign * step_i, ystart, zstart)
                rv = self.initialize_head(xstart + xsign * step_i, ystart, zstart)

        if y != 0:
            ysign = int(y/abs(y))
            ysteps = range(0, ysign*y+1)
            for step_j in ysteps:
                # print(xstart + xsign * xsteps[-1], ystart + ysign * step_j, zstart)
                rv = self.initialize_head(xstart + xsign * xsteps[-1], ystart + ysign * step_j, zstart)
 
        if z != 0:
            zsign = int(z/abs(z))
            zsteps = range(0, zsign*z+1)
            for step_k in zsteps:
                # print(xstart + xsign * xsteps[-1], ystart + ysign * ysteps[-1], zstart + zsign * step_k)
                rv = self.initialize_head(xstart + xsign * xsteps[-1], ystart + ysign * ysteps[-1], zstart + zsign * step_k)

        return rv

    def cursor(self):
        return self.dbits[ self.headx + 1, self.heady + 1, self.headz + 1 ]

    def retrieve(self, x, y, z):
        try:
            return self.dbits[ x, y, z ]
        except KeyError as e:
            return None

    # def x_at_cursor(self):

    def move_head_abs(self, x, y, z):

        if x == self.headx and y == self.heady and z == self.headz and self.last_rv is not None:
            return self.last_rv

        self.last_rv = self.move_head(x-self.headx, y-self.heady, z-self.headz)
        return self.last_rv

    def insert(self, data, x, y, z):
        if verbosity != 0:
            print("\n.")
            print("..")
            print(f"... inserting {data} at ({x}, {y}, {z})")

            print("warning: **** fix this and change to headsize")

        dbit = self.move_head_abs(x-1,y-1,z-1)

        if verbosity != 0:
            print("moved to", dbit)
        
        lbit_idx = dbit.lbit0

        while lbit_idx != lbit_idx.other.other:
            lbit_idx = lbit_idx.other

        dbit = lbit_idx.dbit

        lbit0 = LBit(TimeRoot(), data)
        lbit1 = LBit(TimeRoot(), "time_root")

        newbit = DBit(lbit0, lbit1, x, y, z)
        newbit.set_3d()

        lbit0.x = dbit.lbit0
        lbit1.x = dbit.lbit1

        dbit.lbit0.other = newbit.lbit0
        dbit.lbit1.other = newbit.lbit1

        if verbosity > 5:
            print(newbit)

        self.insert_dbit(newbit)

        return newbit

def inspectDBit(dbit, am :AlgorithmicMemory):
    # if verbosity > 0:
    #    return

    print("Command Prompt Loop")
    print("Available commands: xp (increase x), xm (decrease x), yp (increase y), ym (decrease y), zp (increase z), zm (decrease z), exit (to quit)")

    current_bit = dbit
    print("\nCURRENT_BIT", current_bit)

    while True:
        command = input("Enter a command: ").strip().lower()
      
        if command == 'xp':
            current_bit = current_bit.lbit1.x.dbit
        elif command == 'xm':
            current_bit = current_bit.lbit0.x.dbit
        elif command == 'yp':
            current_bit = current_bit.lbit1.y.dbit
        elif command == 'ym':
            current_bit = current_bit.lbit0.y.dbit
        elif command == 'zp':
            current_bit = current_bit.lbit1.z.dbit
        elif command == 'zm':
            current_bit = current_bit.lbit0.z.dbit
        elif command == 'ot':
            current_bit = current_bit.lbit0.other.dbit
        elif command == 'pr':
            print("printing...")
        elif command == 'cb':
            if current_bit == None:
                current_bit = am.source
            print(latticeModel(current_bit))
        elif command == 'cl':
            lattice.debug_clear()
            current_bit = None
        elif command == 'in1':
            current_bit = lattice.insert("one", 1, 1, 1)
        elif command == 'in01':
            current_bit = lattice.insert("y1", 0, 1, 0)
        elif command == 'in0':
            current_bit = lattice.insert("origin", 0, 0, 0)
        elif command == 'lbin':
            lattice.bot.insert(current_bit)
        elif command == 'rb':
            print("\n".join(current_bit.return_box()))
        elif command == 'lm':
            print(latticeModel())
        elif command == 'exit':
            print("Exiting the loop.")
            return True
        else:
            print("Invalid command. Please use xp, xm, yp, ym, zp, zm, or exit.")
        print("-------------------------------------------------------------------")
        print(current_bit)


# am = AlgorithmicMemory()


# Traverse vector (1,1,1)

# am.move_head(-1, 0, 0)
# am.move_head(0, -1, 0)
# am.move_head(0, 0, -1)
# am.move_head_abs(-4,-4,-4)

# am.move_head(2, 2, 2)

# am.insert("one", 1, 1, 1)
# am.insert("neg_one", -1, -1, -1)

# three = am.insert("three", 3, 3, 3)

# am.insert("neg_one_bottom", -1, -1, -1)

# am.source = three

# i = 0
# max_i = 50

def model_xyz_diagonal(am: AlgorithmicMemory):
    while True:

        try:
            am.i += 1
            sign = [ 'lbit0', 'lbit1' ][random.randint(0, 1)]
            axis = [ 'x', 'y', 'z' ][random.randint(1, 3)-1]

            am.landing = getattr(getattr(getattr(am.source, sign), axis), 'dbit')
            am.target = am.landing
            am.source = am.insert(am.target.lbit0.data + '.' + sign + '.' + axis, am.target.x, am.target.y, am.target.z)
    
        except AttributeError as e:
            if verbosity > 3:
                print(e)
            try:
                am.target = am.insert(am.source.lbit0.data + '.' + sign + '.' + axis, am.source.x, am.source.y, am.source.z)
            except AttributeError as e:
                am.target = am.source


        am.source = am.move_head_abs(am.source.x, am.source.y, am.source.z)

        print(latticeModel(am.source))
        if am.i % 10000 == 0:
            print(am.i)
        # time.sleep(3/16)
        # os.system('clear')
        if am.i > max_i:
            return True

# while True:
#     try:
#         if model_xyz_hypo(am):
#             break
#     except KeyboardInterrupt as e:
#         inspectDBit(am.cursor(), am)

# print("source:")
# print("-------")
# inspectDBit(am.source, am)

# print("target:")
# print("-------")
# inspectDBit(am.target, am)

