import Data.List (foldl')

perms1 :: [a] -> [[a]]
perms1 [] = [[]]
perms1 (x : xs) = [zs | ys <- perms1 xs, zs <- insert x ys]

insert :: a -> [a] -> [[a]]
insert x [] = [[x]]
insert x (y : ys) = (x : y : ys) : map (y :) (insert x ys)

picks :: [a] -> [(a, [a])]
picks [] = []
picks (x : xs) = (x, xs) : [(y, x : ys) | (y, ys) <- picks xs]

perms2 :: [a] -> [[a]]
perms2 [] = [[]]
perms2 xs = [y : zs | (y, ys) <- picks xs, zs <- perms2 ys]

collapse :: [[Int]] -> [Int]
collapse xss = (fst $ foldl' f (id, 0) xss) []
  where
    f (accFun, accSum) xs = if accSum > 0 then (accFun, accSum) else (accFun . (xs ++), accSum + sum xs)

-- collapse [[1], [-3], [2, 4]] = [1]
-- collapse [[-2, 1], [-3], [2, 4]] = [-2, 1, -3, 2, 4]
-- collapse [[-2, 1], [3], [2, 4]] = [-2, 1, 3]