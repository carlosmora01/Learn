import React, { useState } from "react";
import Todo from "./Todo";

export default function TodoList({ todos, todoDelete }) {
  return (
    <div>
      <h1>Soy Todo list</h1>
      {todos.map((todo) => (
        <Todo todo={todo} key={todo.id} todoDelete={todoDelete} />
      ))}
    </div>
  );
}
