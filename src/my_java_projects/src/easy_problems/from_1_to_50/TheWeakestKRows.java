package easy_problems.from_1_to_50;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;

public class TheWeakestKRows {
    public int[] kWeakestRows(int[][] mat, int k) {

        int lenMat = mat.length;

        HashMap<Integer,Integer> mapWeakests = new HashMap<>();

        for (int i = 0; i < lenMat; i++){
            mapWeakests.put(i,sumElements(mat[i]));
        }

        int[] temp = new int[lenMat];
        int j = 0;
        for (int i: mapWeakests.values()){
            temp[j] = i;
            j++;
        }


        Arrays.sort(temp);



        int[] solution = new int[k];
        for (int i = 0; i < k; i++){
            solution[i] = -100;
        }

        for (int l = 0; l < k; l++){

            for (int i = 0; i < lenMat; i++){
                if (mapWeakests.get(i).equals(temp[l]) && !findValue(solution,i) ){
                    solution[l] = i;
                    break;
                }
            }
        }

        return solution;



    }

    private int sumElements(int[] mat){
        int output = 0;
        for (int i = 0; i < mat.length; i++){
            output += mat[i];
        }

        return output;
    }

    private boolean findValue(int[] list, int target){

        for (int num: list ){
            if (num == target) return true;
        }
        return false;
    }
}
