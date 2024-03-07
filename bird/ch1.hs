import Data.List (foldl', inits, tails)

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

takeWhile' :: (a -> Bool) -> [a] -> [a]
takeWhile' p = foldr (\x acc -> if p x then x : acc else []) []

dropWhileEnd' :: (a -> Bool) -> [a] -> [a]
dropWhileEnd' p = foldr (\x acc -> if not (p x) || not (null acc) then x : acc else []) []

integer :: [Int] -> Integer
integer = read . concatMap show

fraction :: [Int] -> Double
fraction = read . ("0." ++) . concatMap show

f1 :: (b -> a -> b) -> b -> [a] -> [b]
f1 f e = map (foldl f e) . inits -- scanl

f2 :: (a -> b -> b) -> b -> [a] -> [b]
f2 f e = map (foldr f e) . tails -- scanr

apply' :: Int -> (a -> a) -> a -> a
apply' 0 f = id
apply' n f = f . apply' (n - 1) f

remove :: (Eq a) => a -> [a] -> [a]
remove e = foldr (\x acc -> if e == x then acc else x : acc) []

perms3 :: (Eq a) => [a] -> [[a]]
perms3 [] = [[]]
perms3 xs = [x : ys | x <- xs, ys <- perms3 (remove x xs)]

concat' :: [[a]] -> [a]
concat' xss = foldl' (\f xs -> f . (xs ++)) id xss []

steep :: [Integer] -> Bool
steep [x] = True
steep xs = fst $ foldr f (True, 0) xs
  where
    f e (accBool, accSum) = (e > accSum && accBool, accSum + e)

-- steep [] = True
-- steep (x : xs) = x > sum xs && steep xs

tails' :: [a] -> [[a]]
tails' [] = [[]]
tails' (x : xs) = (x : xs) : tails' xs

inits' :: [a] -> [[a]]
inits' [] = [[]]
inits' (x : xs) = [] : map (x :) (inits' xs)