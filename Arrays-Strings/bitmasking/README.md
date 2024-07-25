### tricks

- (1 << j) - will right shift 1 by j places

- (1 << j) & mask - will right shift 1 by j places, and with mask => effectively checking if the jth bit is set in mask

-  mask ^ (1 << j) - XOR jth bit of mask with 1 => will toggle the jth bit of mask

- (curr_mask - 1) - will flip all bits after rightmost set bit including right most set bit
                    . doing (curr_mask - 1) & mask iteratively will generate all combinations possible of set bits of mask. 