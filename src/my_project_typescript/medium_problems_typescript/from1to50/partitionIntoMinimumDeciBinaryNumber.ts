function minPartitions(n: string): number {

    if (n.includes("9")){
        return 9
    }
    else if (n.includes("8")){
        return 8
    }else if (n.includes("7")){
        return 7
    }else if (n.includes("6")){
        return 6
    }else if (n.includes("5")){
        return 5
    }else if (n.includes("4")){
        return 4
    }else if (n.includes("3")){
        return 3
    }else if (n.includes("2")){
        return 2
    }else if (n.includes("1")){
        return 1
    }
};