"use client"
import Top from '@/components/top'
import {useState, useEffect} from 'react'

export default function() {
  const [vacancies, setVacancies] = useState([])
  
  return (
    <main>
      <Top><h1>Вакансии</h1></Top>
      <div className="container">
      </div>
    </main>
  );
}
