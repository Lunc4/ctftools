import hashlib
from sys import argv

def md5_hash_integers(start:int, end:int, hash_rounds:int) -> list:
    hashes = []
    for i in range(start,end):
        temp = str(i)   # convert the integer to a string
        for i in range(hash_rounds):
            temp = hashlib.md5(bytes(temp,'ascii')).hexdigest() # hash the integer or hash and return the hexdigest
        hashes.append(temp)
    return hashes;



if __name__ == "__main__":
    arg_names = ['command', 'start', 'end', 'rounds', 'outfile']
    if len(argv) <=3:
        print('[*] Usage:\npython get_x_hash.py starting_point end_point hash_iterations outfile')
        exit()
    args = dict(zip(arg_names,argv))
    start,end,rounds = int(args["start"]),int(args['end']),int(args['rounds']) # retrieve arguments from dict
    
    hashes = md5_hash_integers(start,end,rounds)
    
    if args.get('outfile') != None:
        outfile = args['outfile']
        with open(outfile,'a') as f:
            for hashx in hashes:
                f.write(f'{hashx}\n')
            f.close()
    else:
        print(*hashes,sep='\n')
