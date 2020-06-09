(defun factorial (n &optional (present 1))
    (if (= n 1)
        (return-from factorial present))
    (factorial (1- n) (* n present))
)

(compile 'factorial)
(defun factorial_r (number)
    (if (or (< number 0) (not (= (floor number) (ceiling number))))
        (progn
            (format t "(Recursive) Sorry, but Factorial doesn't exists.")
            (values nil)
        ))
    (factorial number)
)

(defun factorial_nr (number)
    (if (or (< number 0) (not (= (floor number) (ceiling number))))
        (progn
            (format t "(Non-Recursive) Sorry, but Factorial doesn't exists.")
            (return-from factorial_nr nil)
        )
    )
    (defvar fact 1)
    (loop for x from 1 to number do
        (setf fact (* fact x))
    )
    (format t "Factorial without recursion: ")
    (values fact)
)
(compile 'factorial_nr)
(format t "Enter a number: ")
(defvar number (read))

(format t "~d ~%" (factorial_r number))

(format t "~d ~%" (factorial_nr number))
