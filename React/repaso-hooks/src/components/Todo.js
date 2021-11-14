import React from "react";

export default function Todo({ todo, todoDelete }) {
  const { title, description } = todo;
  return (
    <div className="card mt-2">
      <div className="card-body">
        <h3 className="card-title text-right">
          {title}
          <button className="btn btn-sm btn-success ml-2">Terminar</button>
        </h3>
        <p className="card-text text-right"> {description} </p>
        <hr />
        <div className="d-flex justify-content-end">
          <button className="btn btn-sm btn-primary">Editar</button>
          <button
            className="btn btn-sm btn-danger"
            onClick={() => todoDelete(todo.id)}
          >
            Eliminar
          </button>
        </div>
      </div>
    </div>
  );
}
