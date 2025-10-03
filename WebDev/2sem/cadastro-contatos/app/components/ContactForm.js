import { useEffect, useRef, useState } from "react";
import api from "../utils/api";

const ContactForm = ({ onAdd }) => {
  const [form, setForm] = useState({ nome: "", email: "", telefone: "" });
  const nomeInputRef = useRef(null)

  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
      nomeInputRef.current.focus()
  }, [])

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  // const handleSubmit = (e) => {
  //   e.preventDefault();
  //   if (!form.nome.trim()) return; // Validação simples
  //   onAdd({ ...form, id: Date.now() });
  //   setForm({ nome: "", email: "", telefone: "" });
  // };

    const handleSubmit = async (e) => {
    e.preventDefault();
    if (!form.nome.trim()) return; // Validação simples

    try {
      setLoading(true);
      setError(null);

      // Tentar salvar via API primeiro
      try {
        const response = await api.post('/contacts', form);
        // Se API funcionar, usar o ID retornado
        onAdd({ ...form, id: response.data.id });
      } catch (apiError) {
        // Se API falhar, salvar localmente
        console.log('API offline, salvando localmente');
        onAdd({ ...form, id: Date.now() });
      }
      
      setForm({ nome: "", email: "", telefone: "" });
      // Focar novamente no campo nome após adicionar
      nomeInputRef.current?.focus();
      
    } catch (err) {
      setError('Erro ao adicionar contato');
    } finally {
      setLoading(false);
    }
  };

 return (
    <form onSubmit={handleSubmit} className="bg-white shadow rounded p-4 space-y-4">
      <div>
        <label className="block text-sm font-medium mb-1 text-gray-700">Nome</label>
        <input
          ref={nomeInputRef}
          name="nome"
          className="w-full border rounded px-3 py-2 text-gray-900"
          value={form.nome}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label className="block text-sm font-medium mb-1 text-gray-700">Email</label>
        <input
          name="email"
          type="email"
          className="w-full border rounded px-3 py-2 text-gray-900"
          value={form.email}
          onChange={handleChange}
        />
      </div>

      <div>
        <label className="block text-sm font-medium mb-1 text-gray-700">Telefone</label>
        <input
          name="telefone"
          className="w-full border rounded px-3 py-2 text-gray-900"
          value={form.telefone}
          onChange={handleChange}
        />
      </div>

      {/* 🆕 ADICIONAR: Feedback de erro */}
      {error && (
        <div className="text-red-600 text-sm">{error}</div>
      )}

      {/* 🆕 MODIFICAR: Botão com estado de loading */}
      <button 
        type="submit" 
        disabled={loading}
        className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded disabled:opacity-50"
      >
        {loading ? 'Salvando...' : 'Adicionar Contato'}
      </button>
    </form>
  );
};

export default ContactForm;