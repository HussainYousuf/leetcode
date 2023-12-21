subsequence [] = [[]]
subsequence (x : xs) = concat [[ys, x : ys] | ys <- subsequence xs]