%% Specific modules to include in cover.
{
  incl_mods,
  [
   'clj_analyzer',
   'clj_compiler',
   'clj_core',
   'clj_emitter',
   'clj_env',
   'clj_module',
   'clj_namespace',
   'clj_reader',
   'clj_scope',
   'clj_utils',
   'clojerl',
   'clojerl.Boolean',
   'clojerl.Counted',
   'clojerl.Float',
   'clojerl.IColl',
   'clojerl.IDeref',
   'clojerl.IEquiv',
   'clojerl.IFn',
   'clojerl.ILookup',
   'clojerl.IMap',
   'clojerl.IMeta',
   'clojerl.ISeq',
   'clojerl.ISequential',
   'clojerl.Integer',
   'clojerl.Keyword',
   'clojerl.List',
   'clojerl.Map',
   'clojerl.Named',
   'clojerl.Nil',
   'clojerl.Seqable',
   'clojerl.Set',
   'clojerl.String',
   'clojerl.Stringable',
   'clojerl.Symbol',
   'clojerl.Var',
   'clojerl.Vector',
   'clojerl.erlang.Fn',
   'clojerl.erlang.List',
   'clojerl.erlang.Map',
   'clojerl.erlang.Tuple',
   'clojerl.protocol',
   'clojerl.reader.ReaderConditional',
   'cover_report'
  ]
}.
%% Export coverage data for jenkins.
{export, "../logs/cover.data"}.
