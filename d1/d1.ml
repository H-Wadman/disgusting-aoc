let convert str_num =
  match str_num with
  | "one" -> 1
  | "two" -> 2
  | "three" -> 3
  | "four" -> 4
  | "five" -> 5
  | "six" -> 6
  | "seven" -> 7
  | "eight" -> 8
  | "nine" -> 9
  | _ -> failwith "Invalid input"
;;

let length_digit str =
  match str with
  | 1 -> 3
  | 2 -> 3
  | 3 -> 5
  | 4 -> 4
  | 5 -> 4
  | 6 -> 6
  | 7 -> 7
  | 8 -> 8
  | 9 -> 9
  | _ -> failwith "Invalid input"
;;

let text_num str i =
  let rec aux num =
    if num > 9 then None
    else
      try Some (convert (String.sub str i (length_digit num)))
      with _ -> aux (num + 1)
  in
    aux 1
;;

let valid_num str i =
  match int_of_string_opt (String.make 1 (String.get str i))
  with
  | None ->
      text_num str i
  | Some x -> Some x
;;

let cal_val str =
  let rec first str curr =
    match valid_num str curr with
    | None -> first str (curr + 1) 
    | Some x -> string_of_int x
in
  let rec last str curr =
    match valid_num str curr with
    | None -> last str (curr - 1)
    | Some x -> string_of_int x
in
  int_of_string ((first str 0) ^ (last str ((String.length str) - 1)))
;;

let sum_cv file_path =
  let in_stream = open_in file_path
in
  let rec sum curr =
  try 
    let x = cal_val (input_line in_stream)
    in
    Printf.printf "%d\n" x;
    sum (curr + x)
  with End_of_file -> curr
in
  sum 0
;;

let rec last str curr =
  match valid_num str curr with
  | None -> 
    Printf.printf "Pos: %d failed\n" curr;
    last str (curr - 1)
  | Some x -> string_of_int x
;;

let main =
  Printf.printf "%d\n" (sum_cv "input")
;;