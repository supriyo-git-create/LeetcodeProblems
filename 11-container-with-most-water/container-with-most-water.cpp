class Solution {
public:
    int maxArea(vector<int>& height) {
        //optimal approach O(n)
        int maxWater=0;
        int lp=0,rp=height.size()-1;

        while(lp<rp){
            int w=rp-lp;
            int ht=min(height[lp],height[rp]);
            int currWater=w*ht;
            maxWater=max(maxWater,currWater);

            height[lp]<height[rp]?lp++ :rp--;

        }
        return maxWater;
    }
};



 //Brute force approach O(n^2)
        
        // for(int i=0;i<height.size();i++){//i reprn here left wall
        //     for(int j=i+1;j<height.size();j++){//j reprn here right wall
        //         int w=j-i;//right wall - left wall width beriye jabe
        //         int ht=min(height[i],height[j]);
        //         int currWater=w*ht;
        //         maxWater=max(maxWater,currWater);
        //     }
        // }
        // return maxWater;